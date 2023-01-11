# Controller Input

Controllers are a bit more complicated to work with than keyboards. Just sayin'.

### `PadCount()`

This will return the number of controllers. If no controllers are connected, the number `0` will be returned.

### `Pad()`

This command will create a new `pygame._sdl2.controller.Controller()` object for you to use. Make sure you assign it to a variable (e.g. `gamepad = Pad(0)`). It takes one argument: the gamepad's index. Since this is really just a shortcut to a single pygame object, refer to [here](https://www.pygame.org/docs/ref/sdl2_controller.html#pygame._sdl2.controller.Controller) for more info.

<b>TIP</b>: If you're receiving errors when running something like `gamepad.get_button(CONTROLLER_BUTTON_A)`, change `CONTROLLER_BUTTON_A` to `pg.CONTROLLER_BUTTON_A`. Then, when shown in full, it looks like this: `gamepad.get_button(pg.CONTROLLER_BUTTON_A)`. This is because all of the `CONTROLLER_BUTTON` constants are not imported into `nextlib` by default, but they can still be accessed due to how Pygame itself is imported as `pg`, thus allowing Pygame commands to be accessed when `nextlib` is imported globally (and, when not globally, they can still be accessed as `nextlib.pg`).