# Democracy Club design system

Documentation: https://democracyclub.github.io/design-system/

## Use in 3rd party applications

### Python

The design system can be installed using python package managers like `pip` or `pipenv`:

`pip install git+https://github.com/DemocracyClub/design-system.git@VERSION`

It's strongly recommended to pin to a version tag when using in real world applications.

Once installed, all the assets in the `system` directory will be in your `site-packages` folder. To use access them you can import the design system in to your application and use `DC_SYSTEM_PATH`:

```
import dc_design_system
dc_design_system.DC_SYSTEM_PATH
```

You can use this path when compiling the sass by passing it to the include paths.

At this point you can follow the main usage instructions (TODO) to implement.



