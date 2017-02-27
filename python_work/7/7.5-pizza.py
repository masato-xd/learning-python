# coding: utf-8

prompt = ("你想添加什么配料? ")
prompt += "\n可以告诉我'ok',如果你点好了. "

topping = ""
while topping != 'ok':
	topping = raw_input(prompt)
	if topping  != 'ok':
            print "%s add it." % topping
