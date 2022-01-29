# emojiPy

- For use with [gitmoji](https://github.com/carloscuesta/gitmoji-cli), inspired by [emojify](https://github.com/mrowa44/emojify).
- A faster Python emojify tool.
- Emoji data source: https://github.com/github/gemoji/blob/master/db/emoji.json

# Build

```shell
git clone https://github.com/m9810223/emojiPy emojiPy && cd $_
make
```

# Install / Update

```shell
cp emojiPy /usr/local/bin # or any path in $PATH
```

# Speed Comparison

Save 99.43% of time.

```shell
cat test.gitlog | time emojify >/dev/null
# emojify > /dev/null  3.45s user 1.06s system 98% cpu 4.586 total

cat test.gitlog | time emojiPy >/dev/null
# emojiPy > /dev/null  0.02s user 0.00s system 94% cpu 0.026 total
```
