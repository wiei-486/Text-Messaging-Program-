import time
import pyautogui
import pyperclip


RECIPIENT = "name"
MESSAGE = "内容"
SEND_COUNT = 2
SEND_KEY = "enter"
SWITCH_DELAY_SECONDS = 5


def main() -> None:
    if RECIPIENT.startswith("name") or MESSAGE.startswith("内容"):
        raise SystemExit("")
    if not 1 <= SEND_COUNT <= 10:
        raise SystemExit("SEND_COUNT 必须设置为整数。")

    print(f"即将发送给：{RECIPIENT}")
    print(f"发送内容：\n{MESSAGE}")
    print(f"发送次数：{SEND_COUNT}")
    confirmation = input(
        "\n请先在微信中打开并确认对应聊天窗口。"
        "确认后输入 GO 继续，其他输入取消："
    )
    if confirmation != "GO":
        print("已取消，没有发送。")
        return

    pyperclip.copy(MESSAGE)
    print(
        f"\n请在 {SWITCH_DELAY_SECONDS} 秒内切换到微信并点击聊天输入框。"
        "将鼠标移至屏幕左上角可触发安全中止。"
    )
    try:
        for remaining in range(SWITCH_DELAY_SECONDS, 0, -1):
            print(f"{remaining}...")
            time.sleep(1)
        for index in range(SEND_COUNT):
            pyautogui.hotkey("ctrl", "v")
            time.sleep(0.5)
            pyautogui.press(SEND_KEY)
            if index < SEND_COUNT :
                time.sleep(1)
    except KeyboardInterrupt:
        print("\n已中止。")
        return
    except pyautogui.FailSafeException:
        print("\n已触发 PyAutoGUI 安全中止；请检查微信窗口状态。")
        return

    print("发送操作已执行。")


if __name__ == "__main__":
    main()
