PY:=python
obj:=update_emojies emojiPy
all: clean $(obj)
	@chmod +x emojiPy
%: %.py
	@$(PY) $@.py
clean:
	@rm -f $(obj)
test: all
	@git log --graph --pretty='%Cred%h%Creset -%C(auto)%d%Creset %s %Cgreen(%ar) %C(bold blue)<%an>%Creset' --color | emojiPy >/dev/null
	@emojiPy -l >/dev/null
	@emojiPy -h
