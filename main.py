import logging
import tkinter as tk
from cashier import CashierApp


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)


if __name__ == "__main__":
    logger.info("Starting Cashier Application")

    root = tk.Tk()
    app = CashierApp(root)

    root.mainloop()