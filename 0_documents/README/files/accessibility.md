# Visual accessibility

>[Example colour palette]

[WebAIM](https://webaim.org/resources/contrastchecker/) was used to check colour contrast between background and foreground colours.  
Each stated ratio is the contrast ratio between the background and font colours used. Then the pass/fail mode for Web Content Accessibility Guidelines. Each link should provide full details.

| Use | Foreground colour | Background colour | Ratio | WCAG AA | WCAG AAA | Permalink |
|-|-|-|-|-|-|-|
| :heavy_minus_sign: | --color-primary | --color-white | 4.78 : 1 | pass | fail | [Permalink](https://webaim.org/resources/contrastchecker/?fcolor=983BFE&bcolor=FFFFFF) |
| :heavy_multiplication_x: | --color-secondary | --color-white | 1.68 : 1 | fail | fail | [Permalink](https://webaim.org/resources/contrastchecker/?fcolor=38D8FF&bcolor=FFFFFF) |
| :purple_square: | --color-light | --color-white | 3.78 : 1 | fail | fail | [Permalink](https://webaim.org/resources/contrastchecker/?fcolor=9876B0&bcolor=FFFFFF) |
| :heavy_check_mark: | --color-dark | --color-white | 15.21 : 1 | pass | pass | [Permalink](https://webaim.org/resources/contrastchecker/?fcolor=2F1C48&bcolor=FFFFFF) |
| :heavy_minus_sign: | --color-light | --color-black | 5.55 : 1 | pass | fail | [Permalink](https://webaim.org/resources/contrastchecker/?fcolor=9876B0&bcolor=000000) |


# Auditory accessibility

| Object | Method | Description |
|-|-|-|
| `.correct` | `aria-label` | This is the correct answer |
| `.footer-link` | `aria-label` | [link description] (opens in a new tab) |
| `.form-cancel` | `aria-label` | Cancel and return to the previous page |
| `.form-delete` | `aria-label` | Submit the delete [test/answer] form |
| `.form-edit` | `aria-label` | Submit the edit [test/answer] form |
| `.form-new` | `aria-label` | A form to create a new [test/answer] |
| `.form-submit` | `aria-label` | Submit the [test/answer] form |
| `.nav-item` | `aria-current` | page |