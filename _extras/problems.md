---
layout: page
title: Troubleshooting
---

# Common Issues

## Terminal

### "I'm stuck in **Nano**!"

There's a handy reminder at the bottom of the window - `Control-X` allows you to exit **Nano**.
The `^` symbol represents "Hold `Control` and press the following key".

### "I can't copy-paste in the terminal!"

Different systems and even different terminal programs within those systems can take copy-paste differently.
If `Control-C` and `Control-V` don't work, there's a few options to try:

* **Copy:**
  * `Control-Shift-C`.
  * Click and drag with the mouse to select text to copy.
  * Click and drag with the mouse to select text, then right-click and select *"Copy"*.

* **Paste:**
  * `Control-Shift-V`.
  * Click to put the cursor in the right location, then right-click to paste.
  * Click to put the cursor in the right location, then right-click and select *"Paste"*.

### "I ran a command and I'm stuck in the output!"

If their output's too long to show in one go,
some programs (not just **Git**) will let you scroll through it - you should see a `:` at the bottom of the page.

`Up Arrow` and `Down Arrow` will let you go through the output, and `Q` will exit.

### "I ran a command and it's just showing `> `"

You might have failed to finish a quote, e.g. `git commit -m "My message`.
Try `Control-C` to quit the command, or you could enter `"` and then hit enter.
