"""SPA smoke tests (B3.0).

These pin the behaviours a weak future change is most likely to break: the app
shell, hash-route navigation, and the accessibility landmarks. They run against
the real single-file SPA with no data fixtures (its data fetches degrade
gracefully), so they are fast and deterministic.
"""


def test_shell_renders(page, base_url):
    page.goto(base_url + "/")
    assert page.locator("header").is_visible()
    assert page.locator("header nav").count() == 1
    assert page.locator("main#app").count() == 1
    assert page.locator("footer").is_visible()


def test_landing_renders(page, base_url):
    page.goto(base_url + "/")
    page.wait_for_selector("h1")
    assert "translate" in page.locator("h1").first.inner_text().lower()


def test_hash_route_navigation(page, base_url):
    page.goto(base_url + "/")
    page.locator("header nav").get_by_role("link", name="How it works").click()
    page.wait_for_function("location.hash === '#/how-it-works'")
    # The main content region updated to the new view.
    page.wait_for_selector("main#app h1, main#app h2")


def test_nav_has_all_primary_links(page, base_url):
    page.goto(base_url + "/")
    nav = page.locator("header nav")
    for label in ["Dashboard", "Stats", "Open Data", "How it works"]:
        assert nav.get_by_text(label, exact=True).count() >= 1
