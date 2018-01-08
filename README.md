# ogs-batch-analyser
Script that downloads user's games from OGS and analyses them using an external analysis tool like the one found at [lightvector/leela-analysis](https://github.com/lightvector/leela-analysis).
### Example usage
```
ogs-batch-analyser 467993 --skip --number 1 --oldest --command "~/go/leela-analysis/sgfanalyze.py --analyze-thresh .05 --var-thresh .05 --secs-per-search 5 --leela ~/go/leela-analysis/leela_0110_linux_x64_opencl"
Getting game no. 0, on page 1
Downloaded game 9859644
Analysed game 9859644
```
### Installation
Requires python 3.6, addionally uses the *requests* module.
```
git clone
cd ogs-batch-analyser
pip install .
```
### --help output
```
usage: ogs-batch-analyser [-h] [--number NUMBER] [--oldest] [--download-only]
                          [--skip] [--command COMMAND]
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
