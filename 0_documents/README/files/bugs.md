| # | Date IDd | Bug description | Date resolved | Resolution | Commit |
|-|-|-|-|-|-|
| 1 | 2026-10-22 | `<img src="{{ MEDIA_URL }}st2026.jpg">` or with `showtimes/` does not show the image | 2026-10-27 | `<img src="{{ product.image }}"` pulls from Stripe src | [main 0be9757] dynamic showtime/product page |
| 2 | 2026-10-27 | Heroku live site application error log: `code=H14` | 2026-10-28 | Heroku Eco dyno ~~not~~ activated | N/A |
| 3 | 2026-10-28 | Heroku live site HTTP 500 error ||||
| 4 | 2026-11-02 | Heroku live site static media not loading ||||
| 5 | 2026-11-03 | Andy Jud walkthrough project was working before bug#2, now the "Add to cart" button being built in _cart-button.html_ (_showtime.html_) doesn't send a Cart.cart_session request | 2026-11-04 | _base.html_ `<body hx-headers="{'x-csrftoken': '{{ csrf_token }}'}">` seems to be incompatible, despite coming from the official docs | [main 4647b48] REMOVE <body hx-headers='{'x-csrftoken': '{{ csrf_token }}'}'> |
| 6 | 2026-11-05 | _checkout-total.html_ `div#product-total-{{product.id}}` is not functioning without page reload ||||
| 7 | 2026-11-08 | _cart.html_ `<input name="disk">` doesn't function (hoping related to bug#6) ||||