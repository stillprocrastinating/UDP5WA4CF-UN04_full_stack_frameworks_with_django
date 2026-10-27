I decided to follow Andreas Juds' Django startup tutorial, so that I could then follow his Stripe tutorial later on, as the Code Institute lessons are outdated.


# [Django startup tutorial](https://www.youtube.com/watch?v=SQ4A7Q6_md8)

```
href="{{ request.META.HTTP_REFERER }}"
```

Wow, this would've been easier, if I knew about it, than the [JavaScript version](https://github.com/stillprocrastinating/UDP5WA4CF-UN03_back_end_development/blob/main/0_static/js/script.js#L168) I implemented in my [milestone 3 project](https://github.com/stillprocrastinating/UDP5WA4CF-UN03_back_end_development/tree/main).


# [Stripe tutorial](https://www.youtube.com/watch?v=IzxNNWjYsPk&list=PL5E1F5cTSTtRwWj43zbcl5d-e2c1f1M9q)

```
return redirect(f'{settings.BASE_URL}{reverse("new_page")}?next={request.get_full_path()}')
```

This code renders the redirect to a new page (for example, a login page) then redirects back to the original page for seamless user interface experience. Again, something I wanted for my [milestone 3 project](https://github.com/stillprocrastinating/UDP5WA4CF-UN03_back_end_development/tree/main).

### note

a_stripe = shows
products = showtime
UserPayment = StripeOnePayment
...
subscribe = lessons


timestamp = part 3