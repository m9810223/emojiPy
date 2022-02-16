# emojiPy

- For use with [gitmoji-cli](https://github.com/carloscuesta/gitmoji-cli), inspired by [emojify](https://github.com/mrowa44/emojify).
- A faster Python emojify tool.
- Emoji data source: https://github.com/github/gemoji/blob/master/db/emoji.json

---

## Install

- (recommended) Download & Install
  ```shell
  wget https://raw.githubusercontent.com/m9810223/emojiPy/master/emojiPy \
      -O /tmp/emojiPy && chmod +x $_ && cp $_ /usr/local/bin
  ```
- or Clone & Build & Install
  ```shell
  git clone https://github.com/m9810223/emojiPy emojiPy && cd $_
  make
  cp emojiPy /usr/local/bin
  ```

## Speed Comparison

Save `99.43%` of time.

```shell
cat test.gitlog | time emojify > /dev/null
# emojify > /dev/null  3.45s user 1.06s system 98% cpu 4.586 total

cat test.gitlog | time emojiPy > /dev/null
# emojiPy > /dev/null  0.02s user 0.00s system 94% cpu 0.026 total
```

## Alias for `git log`

```shell
alias glol="git log --graph --pretty='%Cred%h%Creset -%C(auto)%d%Creset %s %Cgreen(%ar) %C(bold blue)<%an>%Creset' --color | emojiPy | less"
```

## CLI

```shell
Faster 🚀 Python 🐍 emojify 🤗

Usage:  emojiPy [OPTIONS] [INPUT]

Options:
    -l, --list     List all emojies.
    -r, --random   Print a random emoji.
```
