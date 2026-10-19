# https://youtu.be/xQUCk_i0htE?si=eV-qWxrIuJ8yq2hQ&t=613

return redirect(f'{settings.BASE_URL}{reverse("new_page")}?next={request.get_full_path()}')
# this code renders the redirect to a new page (for example, a login page) then redirects back to the original page for seamless user interface experience
