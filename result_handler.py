import os
import datetime
from browser_use.agent.views import AgentHistoryList

def process_result(task_prompt: str, result_history: AgentHistoryList, out_dir: str = "outputs", extension: str = "md"):
    """
    Agentが返した結果(AgentHistoryList)を、必要に応じて加工/ログを残す処理。
    ここではシンプルに最終結果(final_result)を取り出してファイル出力する。
    """
    # まずは最終結果を取得 (str or None)
    final_output = result_history.final_result()

    # final_result() が None の場合もあり得るのでハンドリング
    if not final_output:
        final_output = "No final result found."

    # 別の用途で、history全体を解析することも可能
    # e.g. print(result_history.urls()) など

    # 最終的にファイルへ書き込む
    write_result_to_file(task_prompt, final_output, out_dir, extension)

def write_result_to_file(task_prompt: str, final_output: str, out_dir: str, extension: str):
    """
    結果をファイルに書き込む。
    日時を含むファイル名を自動生成し、タスクプロンプトと合わせて出力。
    """
    # 出力先フォルダを作成（存在しなければ）
    os.makedirs(out_dir, exist_ok=True)

    # 日時入りのファイル名
    timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    filename = f"{timestamp}-output.{extension}"
    filepath = os.path.join(out_dir, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        if extension.lower() == "md":
            f.write("# Browser Use Agent Result\n\n")
            f.write("## Task Prompt\n")
            f.write(f"{task_prompt}\n\n")
            f.write("## Final Result\n")
            f.write(final_output)
        else:
            # txtなど他の拡張子の場合はシンプルに書き込み
            f.write(f"Task Prompt:\n{task_prompt}\n\n")
            f.write("Final Result:\n")
            f.write(final_output)

    print(f"結果をファイルに保存しました: {filepath}")
