# ogs-batch-analyser
Script that downloads user's games from OGS and analyses them.
### Example usage
```
[idex@ide ogs-batch-analyser]$ python ogs-batch-analyser.py 467993 -s -n 1 -o -c "~/go/leela-analysis/sgfanalyze.py --analyze-thresh .05 --var-thresh .05 --secs-per-search 5 --leela ~/go/leela-analysis/leela_0110_linux_x64_opencl" 
Getting game no. 0, on page 1
Downloaded game 9859644
Analysed game 9859644
```
### Installation
In the main directory run 
`pip install .`
### --help output
```
usage: ogs-batch-analyser.py [-h] [--number NUMBER] [--oldest]
                             [--download-only] [--skip] [--command COMMAND]
                             user

Script that downloads user's games from OGS and analyses them.

positional arguments:
  user                  User id of the user whose games you want to download
                        (example: 123456)

optional arguments:
  -h, --help            show this help message and exit
  --number NUMBER, -n NUMBER
                        Number of games to download (default=10)
  --oldest, -o          Start downloading from the oldest game (by default
                        downloads from latest)
  --download-only, -d   Download without analysis
  --skip, -s            Skip the analysis of the other player
  --command COMMAND, -c COMMAND
                        Command for the tool used for the analysis
```
