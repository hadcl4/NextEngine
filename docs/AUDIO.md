# Playing Audio

Something to know before getting into this section much is the difference between the terms `Music` and `Sound` in `nextlib`. Any commands having to do with `Music` will loop infinitely, unless manually stopped, whereas commands having to do with `Sound` won't loop at all.

You can import audio into your project either manually through a file manager (just copy and paste a `.ogg` file into your project's `music` folder) or from NextEngine's "Assets" tab.

### `PlayMusic()`

This function will began the playback of `Music`. It takes one argument: the name of the audio file you want to play. The audio file MUST be `.ogg`! You are only able to have one `Music` file playing at once.

Example: `PlayMusic("theme_song")`

### `StopMusic()`

This will stop the currently playing `Music`. No arguments.

### `PlaySound()`

This function will playback a `Sound`. Like `PlayMusic()`, the only argument it needs is the name of the file it will play. However, unlike `PlayMusic()`, there is no way to manually stop the `Sound`'s playback. It will stop after it has finished the playback for the first time.

Example: `PlaySound("jump")`