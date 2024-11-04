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

Images and fonts can be found at `dc_design_system.DC_SYSTEM_PATH + "static"` + [fonts|images]. The final css should live in a directory with fonts and images in the parent directory:

```
- css/
    - processed_from_design_system.css
- fonts/
    - [fonts from design system]
- images/
    - [images from design system] 
```

At this point you can follow the main usage instructions (TODO) to implement.

#### Django

If you are using Django, you should include `dc_design_system` in your INSTALLED_APPS. This will ensure `collectstatic` picks up the fonts and images. You will still need to tell `libsass` about the `DC_SYSTEM_PATH

### Versioning

After making changes to the design system: 
1. Bump the version number in package.json according to the semver system (https://semver.org/)
2. Take that version number and, in the GitHub UI make a new release with that version and a description of the work.
3. Update the requirement version in projects that use the package.

Viewing and compiling edits: 

`npm run build`
`npm start`

# Hosted static assets

This project is designed to be included in projects and for their existing 
pipelines to deal with serving assets.

There are some cases (e.g 500 pages) when we want to render a very simple 
page that still uses the design system.

Because the asset pipeline may well be the thing that causes a 500, we don't 
want to rely on a project's pipeline to render the 500 page.

To that end, we make a serve a small version of the design system at
`http://dc-shared-frontend-assets.s3-website.eu-west-2.amazonaws.com/styles.css`.

That bucket is manually maintained at the moment, and the CSS file is the 
output of `npm run build:sass-core`. To update this file, run that command 
and manually upload it to the S3 bucket in the DC shared production AWS 
account. 
