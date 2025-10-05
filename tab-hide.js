/**
 * USAGE:
 * 1) Open the tab you want to disguise (e.g. your GitHub tab).
 * 2) Press F12 (or Ctrl+Shift+I) → Console.
 * 3) Paste the whole code below and press Enter.
 * 4) When prompted, type the new tab title and press OK.
 * 5) When prompted for favicon URL:
 *    - Enter a favicon URL to set a custom icon, OR
 *    - Leave blank (press OK) to remove the icon entirely (we add a transparent icon).
 *
 * NOTE: This runs only in the current tab (you cannot change other tabs from here).
 * The change is temporary (page reload will revert unless you re-run).
 * Use responsibly.
 */

(function () {
  try {
    // ask for new title
    let newTitle = prompt("Enter the new tab title (e.g. NotYourBusiness):");
    if (newTitle && newTitle.trim().length) {
      document.title = newTitle.trim();
    }

    // remove all existing favicons (works even if there are many <link rel="icon"> tags)
    document.querySelectorAll("link[rel~='icon']").forEach((n) => n.remove());

    // prompt for favicon URL (optional). Leave blank to hide icon.
    let favURL = prompt(
      "Enter favicon URL to use (leave blank to hide icon):",
      ""
    );
    if (favURL && favURL.trim().length) {
      // add the provided favicon
      const l = document.createElement("link");
      l.rel = "icon";
      l.href = favURL.trim();
      document.head.appendChild(l);
    } else {
      // add a tiny transparent favicon so the tab shows a blank icon
      const blank = document.createElement("link");
      blank.rel = "icon";
      blank.href =
        "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR4nGMAAQAABQABDQottAAAAABJRU5ErkJggg==";
      document.head.appendChild(blank);
    }

    // restore original title on focus
    const original = document.title; // we keep the current (disguised) title for simplicity
    window.addEventListener("focus", function restore() {
      // optional: if you want to auto-restore on focus, uncomment the next line
      // document.title = originalTitleSavedEarlier;
      // window.removeEventListener("focus", restore); // if you want one-time restore
      // for now we do nothing so the disguised title stays until reload
    });

    alert(
      "Tab title updated and favicon removed/changed. Reload will revert changes."
    );
  } catch (e) {
    console.error("Error running disguise script:", e);
  }
})();
