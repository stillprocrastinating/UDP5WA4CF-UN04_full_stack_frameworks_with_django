# https://www.youtube.com/watch?v=SQ4A7Q6_md8

I decided to follow Andreas Juds' Django startup tutorial, so that I could then follow his Stripe tutorial later on, as the Code Institute lessons are outdated.

timestamp = 11:10


# https://youtu.be/xQUCk_i0htE?si=eV-qWxrIuJ8yq2hQ&t=613

```
return redirect(f'{settings.BASE_URL}{reverse("new_page")}?next={request.get_full_path()}')
```

This code renders the redirect to a new page (for example, a login page) then redirects back to the original page for seamless user interface experience
