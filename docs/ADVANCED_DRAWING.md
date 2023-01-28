# Advanced Drawing Functions

The `nextlib` library has more drawing functions than what are featured in "The Basics".

### `SetTransparency()`

This will cause sprites drawn onto the surface to appear somewhat transparent. It works best with moving sprites. Only one argument is required: a number between `0` and `255`. The lower, the more transparent.

Example: `SetTransparency(122)`

### `RenderBlank()`

You can use this function as an alternative to `DrawBackdrop()`. Used in the exact same way, other than it doesn't take any arguments. As the name suggests, this will render a "blank" backdrop, without a sprite.

### `RenderSprite()`

This is an alternative to `DrawSprite()`, using Pygame's default coordinate plain. Takes 3 arguments, all of which are the same as `DrawSprite()`'s arguments. Good for if you want to position text with a moving sprite.

Example: `RenderSprite("coin",150,270)`
