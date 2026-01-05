COUNTER_APP_HTML = """
<!doctype html>
<html lang=\"en\">
  <head>
    <meta charset=\"utf-8\" />
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
    <title>Playwright Click Test Sample</title>
    <style>
      body { font-family: sans-serif; padding: 16px; }
      button { padding: 8px 12px; }
      #count { font-weight: 700; }
      .row { margin: 12px 0; }
    </style>
  </head>
  <body>
    <h1>Sample UI</h1>

    <div class=\"row\">
      <div>Count: <span id=\"count\">0</span></div>
      <button id=\"inc\">Increment</button>
      <button id=\"dec\">Decrement</button>
    </div>

    <div class=\"row\">
      <label>
        <input id=\"agree\" type=\"checkbox\" />
        Agree
      </label>
      <div id=\"agree_status\">Not agreed</div>
    </div>

    <div class=\"row\">
      <button id=\"toggle\">Toggle message</button>
      <div id=\"message\" style=\"display:none\">Hello!</div>
    </div>

    <script>
      (function () {
        const countEl = document.getElementById('count');
        const incBtn = document.getElementById('inc');
        const decBtn = document.getElementById('dec');

        function setCount(n) {
          countEl.textContent = String(n);
        }

        incBtn.addEventListener('click', () => {
          setCount(Number(countEl.textContent) + 1);
        });

        decBtn.addEventListener('click', () => {
          setCount(Number(countEl.textContent) - 1);
        });

        const agree = document.getElementById('agree');
        const agreeStatus = document.getElementById('agree_status');
        agree.addEventListener('click', () => {
          agreeStatus.textContent = agree.checked ? 'Agreed' : 'Not agreed';
        });

        const toggle = document.getElementById('toggle');
        const message = document.getElementById('message');
        toggle.addEventListener('click', () => {
          const shown = message.style.display !== 'none';
          message.style.display = shown ? 'none' : 'block';
        });
      })();
    </script>
  </body>
</html>
"""
