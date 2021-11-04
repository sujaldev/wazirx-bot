# Wazirx Bot

Wazirx bot written in python with selenium

#### What can it do?

Mostly anything that you can do on [Wazirx web](https://www.wazirx.com).\
Except login/signup. Login support will be added in the future. \
Since signup is mostly a one time process, users should create account first \
and then use the library.

## How to use interaction_lib

```python
from src.interaction_lib.interactions import WazirxWeb

WazirxWeb().start_console()
```

This will start a loop where in you can enter commands. \
Sample:

```
>>> lb search doge
>>> lb clear_search
>>> rb switch_to_sell_tab
```

> ### Usage:
> board command &#91;&lt;argument&gt;&#93;
> ###### Where board can either be:
> `lb` for left-hand side board \
> `rb` for right-hand side board

![Left Board Diagram](https://sujaldev.github.io/wazirx-bot/assets/left/left-board.png) <br>
Commands for lb (left-board):

- `switch_base_currency` argument: string containing INR, USDT, WRX or BTC
- `sort_by` argument: string containing pair, volume or change
- `search` argument: crypto currency code
- `clear_search`
- `get_currency_dict`
- `switch_currency` argument: string in format CRYPTO-BASE, example: DOGE-INR

Commands for rb (right-board):

- `switch_to_open_orders`
- `switch_to_completed_orders`
- `switch_to_buy_tab`
- `switch_to_sell_tab`
- `input_at_price` argument: new price value
- `input_amount` argument: new buy amount value
- `input_total` argument: new balance to spend value
- `buy_sell_button` HINT: buy or sell is dependent on which tab is open
