#!/bin/env python3
import requests
import json
import subprocess
import os
import argparse

command = os.path.expanduser(
    f"~/go/leela-analysis/sgfanalyze.py --analyze-thresh .05 --var-thresh .05 --secs-per-search 5 --leela ~/go/leela-analysis/leela_0110_linux_x64_opencl")


def save(fname='', source=b''):
    with open(fname, 'w') as f:
        f.write(source.decode('utf8'))


def process_games(
        user=123456,
        total=1,
        latest=True,
        download_only=False,
        skip=False):
    page = 1
    if latest:
        user_games_json = requests.get(
            f'http://online-go.com/api/v1/players/{user}/games?ordering=-id')
    else:
        user_games_json = requests.get(
            f'http://online-go.com/api/v1/players/{user}/games')
    try:
        user_games = json.loads(user_games_json.content)
    except json.decoder.JSONDecodeError as e:
        print(user_games_json.headers)
        raise e
    for number in range(total):
        if number >= page * 10:
            page += 1
            user_games_json = requests.get(f'{user_games["next"]}')
            user_games = json.loads(user_games_json.content)
        print(f'Getting game no. {number}, on page {page}')
        try:
            game = user_games['results'][number % 10]
        except IndexError as e:
            print(f'No game found! game number: {number}, on page: {page}')
            continue
        sgf = requests.get(
            f'https://online-go.com/api/v1/games/{game["id"]}/sgf/')
        game_name = f'{game["id"]}'
        save(f'{game_name}.sgf', sgf.content)
        print(f'Downloaded game {game["id"]}')

        if download_only:
            continue

        skip_who = 'white' if game['black'] == user else 'black'
        cmd = command
        if skip:
            cmd += f' --skip-{skip_who}'
        cmd += f' {game_name}.sgf'
        ret = subprocess.run(
            cmd,
            shell=True,
            stderr=subprocess.PIPE,
            stdout=subprocess.PIPE)
        save(f'{game_name}-processed.sgf', ret.stdout)
        print(f'Analysed game {game["id"]}')


parser = argparse.ArgumentParser(
    description='Script that downloads user\'s games from OGS and analyses them.')
parser.add_argument(
    'user',
    help='User id of the user whose games you want to download (example: 123456)')
parser.add_argument(
    '--number', '-n',
    help='Number of games to download (default=10)',
    type=int,
    default=10)
parser.add_argument(
    '--oldest', '-o',
    help='Start downloading from the oldest game (by default downloads from latest)',
    action='store_false')
parser.add_argument(
    '--download-only', '-d',
    help='Download without analysis',
    action='store_true')
parser.add_argument(
    '--skip', '-s',
    help='Skip the analysis of the other player',
    action='store_true')
parser.add_argument(
    '--command', '-c',
    help='Command for the tool used for the analysis')
args = parser.parse_args()
if args.command:
    command = os.path.expanduser(args.command)
process_games(
    user=args.user,
    total=args.number,
    latest=args.oldest,
    download_only=args.download_only,
    skip=args.skip)
