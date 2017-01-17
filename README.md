> **Starting 3.0.0** `zz File Icons` will be renamed to `A File Icon`. I've found the way how to fix/implement [#23](https://github.com/ihodev/sublime-file-icons/issues/23), [#24](https://github.com/ihodev/sublime-file-icons/issues/24). I have no plans to add new icons in 3.0.0, it will bring only the new way of applying them. I apologize for any inconvenience caused.

# ![A File Icon][img-logo]

[![Release][img-release]][release]
[![Downloads][img-downloads]][downloads]
[![Make a donation at patreon.com][img-patreon]][patreon]
[![Share via Twitter][img-twitter]][twitter]

This package adds file specific icons to Sublime Text for improved visual grepping. It's heavily inspired by [Atom File Icons][atom-file-icons].

Its aims are:

* To be a `tmPreferences` storage for UI themes that support file icons.
* To provide file type icons for themes those don't (fully) support file icons.

If you have any problems, please search for a similar issue first, before creating [a new one][new-issue]. 

> Also, check the list of [known issues][known-issues] before doing so.

## Users

<!--
### Getting Started

[![Getting Started with A File Icon][img-getting-started]][getting-started]
-->

### Installation

#### Package Control

The easiest way to install is using Sublime's [Package Control][downloads]. It's listed as `A File Icon`.

1. Open `Command Palette` using menu item `Tools → Command Palette...`
2. Choose `Package Control: Install Package`
3. Find `A File Icon` and hit `Enter`

#### Download

1. [Download the `.zip`][release]
2. Unzip and rename folder to `A File Icon`
3. Copy folder into `Packages` directory, which you can find using the menu item `Preferences → Browse Packages...`

> **Note:** Don't forget to restart Sublime Text after installing this package. 

### Customization

You can change the color, opacity level and size of the icons by modifying your user preferences file, which you can find by:

* `Preferences → Package Settings → A File Icon → Settings`,
* Choose `A File Icon: Settings` in `Command Palette`.

### Themes

If your theme supports `A File Icon` you can choose what icons you want to use – provided by the theme (by default) or provided by the package. Otherwise this package adds its own icons only.

Themes that already have support of `A File Icon` include:

* [Boxy Theme][boxy-theme]
* [Material Theme][material-theme]

### Troubleshooting

If something goes wrong try to:

1. Open `Command Palette` using menu item `Tools → Command Palette...`.
2. Choose `A File Icon: Clean Up`.
3. Restart Sublime Text.

#### Wrong Icons

Sublime Text file type icons use syntax scopes. That's why icons for packages provided by the community require to be installed.

See the list of [custom packages][packages] that you may need to install to see the right icon.

#### Missing Icons

In some cases you may see that some icons from your current theme are missing. You can:

- Request support for this package from the theme's developer.
- Submit a request to add missing icons if the theme already does.

[More details here →][details] 

#### Sublime Linter Setup

This package adds some syntax aliases which Sublime Linter doesn't recognize. Just update your Sublime Linter settings, e.g.:

```js
  "syntax_map": {
    "html (django)": "html",
    "html (rails)": "html",
    "html 5": "html",
    "javascript (babel)": "javascript",
    "javascript (gruntfile)": "javascript",
    "javascript (gulpfile)": "javascript",
    "json (bower)": "json",
    "json (npm)": "json",
    "json (settings)": "json",
    "magicpython": "python",
    "php": "html",
    "python django": "python",
    "pythonimproved": "python"
  },
```

Full list of syntax aliases can be found [here][aliases].

## Developers

### Bring Support to Your Theme

If you are a theme developer and you want to support `A File Icon`, you should:

* Remove all stuff related to the icon setup: `.tmPreferences`, `.sublime-settings` and `.tmLanguage` files.
* Rename all your icons to match [these ones][icons].
* Add `.st-file-icons` file to the root of your theme (this is how we check if the theme is **supported**).

### How It Works

In simple terms, `A File Icon` does the following:

1. Searches all installed and supported themes.
2. Checks if themes that don't support it are already patched, if not
3. Patches them by:
    - Generating `<theme-name>.sublime-theme` files from a [template][template].
    - Putting them into `dist/patches/` directory.
4. For themes that support it, provides `.tmPreferences` files by default (user can override icons provided by the theme via `"force_override": true`)
5. After restarting Sublime Text, the patched themes will be updated to use the icons provided by `A File Icon`

It does these steps when:

- You install it.
- Plugins are loaded.
- You change its preferences.

The real process is just a little bit more complex to minimize hard drive I/O.

### Contributing

Want to contribute some code? Excellent! Read up on our [guidelines][contributing].

Together we will make **A File Icon** even better than it is today!

## Resources

### Colors

Colors are from the [Boxy Theme][boxy-theme] icon color palette. They are bright because they should look good with most themes. However you can change color and opacity level of all icons. See [customization][customization].

![Palette][img-palette]

### Icons

This package contains icons provided by:

- [Atom File Icons][atom-file-icons]
- [Boxy Theme][boxy-theme]
- [Devicons][devicons]
- [Font Awesome][font-awesome]
- [Font Mfizz][font-mfizz]
- [Icomoon][icomoon]
- [Octicons][octicons]

Source icons are provided in SVG format (Sublime Text doesn't currently support it). We convert them to @1x, @2x and @3x PNG assets before each release via a custom `gulp` task. 

Rasterized icons can be found in `dist/patches` folder.

## Change Log

See [CHANGELOG.md][changelog].

## Known Issues

1. This package requires you to restart Sublime Text for the applied icons to take effect when:
    - you install it,
    - you change its preferences,
    - you install a new theme that should be patched.
2. The icons for custom packages need to be installed. E.g. if you want to see `SCSS` icon you should install one of the `SCSS` syntax packages.

## Share The Love

I've put a lot of time and effort into making **A File Icon** awesome. If you love it, you can buy me a coffee. I promise it will be a good investment 😉.

**Donate with:** [Patreon][patreon].

<!-- Resources -->

[atom-file-icons]: https://github.com/DanBrooker/file-icons
[boxy-theme]: https://github.com/ihodev/sublime-boxy
[devicons]: http://vorillaz.github.io/devicons/#/main
[font-awesome]: http://fontawesome.io/
[font-mfizz]: http://fizzed.com/oss/font-mfizz
[icomoon]: https://icomoon.io/
[material-theme]: https://github.com/equinusocio/material-theme
[octicons]: https://octicons.github.com/

<!-- Misc -->

[aliases]: https://github.com/ihodev/sublime-file-icons/tree/dev/dist/languages
[bring-support]: https://github.com/ihodev/sublime-file-icons#bring-support-to-your-theme
[changelog]: https://github.com/ihodev/sublime-file-icons/blob/dev/CHANGELOG.md
[coming-soon]: https://github.com/wbond/package_control_channel/pull/5852
[contributing]: https://github.com/ihodev/sublime-file-icons/blob/dev/.github/CONTRIBUTING.md
[customization]: https://github.com/ihodev/sublime-file-icons#customization
[details]: https://forum.sublimetext.com/t/sublime-text-3-file-icons-in-sidebar/21134/4
[downloads]: https://packagecontrol.io/packages/A%20File%20Icon
[getting-started]: https://youtu.be/bTIOL-5SxHY 'Watch "Getting Started with A File Icon" on YouTube'
[icons]: https://github.com/ihodev/sublime-file-icons/tree/dev/dist/patches/icons
[known-issues]: https://github.com/ihodev/sublime-file-icons#known-issues
[new-issue]: https://github.com/ihodev/sublime-file-icons/issues/new
[packages]: https://github.com/ihodev/sublime-file-icons/blob/dev/PACKAGES.md
[patreon]: https://www.patreon.com/ihodev
[release]: https://github.com/ihodev/sublime-file-icons/releases
[template]: https://github.com/ihodev/sublime-file-icons/blob/dev/util/tpl.py
[issues]: https://github.com/ihodev/sublime-file-icons/issues
[twitter]: https://twitter.com/intent/tweet?hashtags=sublimetext%2C%20file%2C%20icons&ref_src=twsrc%5Etfw&text=A%20File%20Icon%20%E2%80%93%20Sublime%20file%20icons%20for%20improved%20visual%20grepping%20%F0%9F%8E%89&tw_p=tweetbutton&url=https%3A%2F%2Fgithub.com%2Fihodev%2Fsublime-file-icons&via=ihodev

<!-- Assets -->

[img-downloads]: https://img.shields.io/packagecontrol/dt/A%20File%20Icon.svg?maxAge=3600&style=flat-square
[img-getting-started]: https://raw.githubusercontent.com/ihodev/sublime-file-icons/dev/media/getting-started.png
[img-logo]: https://raw.githubusercontent.com/ihodev/sublime-file-icons/3.0.0/media/logo.png
[img-patreon]: https://rawgit.com/ihodev/sublime-file-icons/3.0.0/media/donate.svg
[img-release]: https://img.shields.io/github/release/ihodev/sublime-file-icons.svg?maxAge=86400&style=flat-square
[img-palette]: https://raw.githubusercontent.com/ihodev/sublime-file-icons/dev/media/palette.png
[img-twitter]: https://rawgit.com/ihodev/sublime-file-icons/3.0.0/media/twitter.svg
