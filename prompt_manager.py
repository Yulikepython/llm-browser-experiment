import importlib
import os
import sys
from typing import Optional

def load_prompt_by_name(prompt_name: str) -> str:
    """
    指定された名前から対応するtask_promptを取得して返す。
    - prompts/sample_promptX などサンプル
    - my_prompts/personal_promptX など個人用
    prompt_name はファイル名 (拡張子除く) を想定。

    例:
      "sample_prompt1" -> prompts/sample_prompt1.py のtask_prompt
      "personal_prompt1" -> my_prompts/personal_prompt1.py のtask_prompt
    """
    # まず、prompts/ 下を探す
    module_path = f"prompts.{prompt_name}"
    if module_exists(module_path):
        return import_task_prompt(module_path)

    # 次に、my_prompts/ 下を探す
    module_path = f"my_prompts.{prompt_name}"
    if module_exists(module_path):
        return import_task_prompt(module_path)

    # 見つからない場合は例外
    raise FileNotFoundError(f"Prompt file '{prompt_name}.py' not found in prompts/ or my_prompts/")


def import_task_prompt(module_path: str) -> str:
    """
    指定モジュールをimportし、task_prompt変数を読み取って返す。
    事前にmodule_existsで存在チェックしている前提。
    """
    try:
        module = importlib.import_module(module_path)
        # モジュール内に "task_prompt" が定義されているかチェック
        if not hasattr(module, "task_prompt"):
            raise AttributeError(f"No 'task_prompt' found in {module_path}.py")
        return getattr(module, "task_prompt")
    except Exception as e:
        # 例外があればラップして投げ直す
        raise ImportError(f"Failed to import {module_path}: {e}")


def module_exists(module_name: str) -> bool:
    """
    importlib.util.find_spec でモジュールの存在を確認する。
    """
    import importlib.util
    spec = importlib.util.find_spec(module_name)
    return spec is not None


def get_prompt_from_env_or_arg() -> Optional[str]:
    """
    1. コマンドライン引数からprompt名を指定 (python main.py sample_prompt1)
    2. 環境変数PROMPT_NAME から取得
    いずれも無ければNoneを返す
    """
    # コマンドライン引数で指定
    if len(sys.argv) > 1:
        return sys.argv[1]

    # 環境変数で指定
    env_prompt_name = os.environ.get("PROMPT_NAME")
    if env_prompt_name:
        return env_prompt_name

    return None
