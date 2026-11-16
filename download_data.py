"""Скачивает датасет M5 Forecasting (Kaggle) в data/raw/.

Использование:
    python download_data.py

Требования:
    - pip install kaggle  (уже в requirements.txt)
    - API-токен ~/.kaggle/kaggle.json
      (kaggle.com -> аватар -> Settings -> API -> Create New Token)
    - принятое соглашение на вкладке Rules страницы соревнования
      https://www.kaggle.com/competitions/m5-forecasting-accuracy

Альтернатива без API: скачай ZIP вручную через кнопку Download All на вкладке
Data страницы соревнования и распакуй в data/raw/ — скрипт увидит файлы и
не будет качать повторно.
"""

from pathlib import Path
import subprocess
import sys
import zipfile

COMPETITION = "m5-forecasting-accuracy"
RAW_DIR = Path("data/raw")
# Файлы, без которых проект не работает: проверяем их наличие
KEY_FILES = ["sales_train_validation.csv", "calendar.csv", "sell_prices.csv"]


def main() -> None:
    RAW_DIR.mkdir(parents=True, exist_ok=True)

    # 1. Идемпотентность: если данные уже есть, ничего не делаем.
    missing = [f for f in KEY_FILES if not (RAW_DIR / f).exists()]
    if not missing:
        print("Данные уже на месте, скачивание не требуется.")
        return
    print(f"Не хватает файлов: {', '.join(missing)}")

    # 2. Проверяем токен Kaggle до запуска скачивания — иначе ошибка CLI непонятна.
    token = Path.home() / ".kaggle" / "kaggle.json"
    if not token.exists():
        sys.exit(
            "Не найден ~/.kaggle/kaggle.json.\n"
            "Скачай API-токен: kaggle.com -> аватар -> Settings -> API -> "
            "Create New Token, положи kaggle.json в ~/.kaggle/ "
            "(Linux/macOS: chmod 600 ~/.kaggle/kaggle.json).\n"
            "Или скачай файлы вручную со страницы соревнования (см. docstring)."
        )

    # 3. Скачивание через официальный CLI Kaggle.
    print(f"Скачиваю {COMPETITION} (около 100 МБ)...")
    subprocess.run(
        ["kaggle", "competitions", "download", "-c", COMPETITION, "-p", str(RAW_DIR)],
        check=True,
    )

    # 4. Распаковываем архив, если CLI скачал один ZIP.
    archive = RAW_DIR / f"{COMPETITION}.zip"
    if archive.exists():
        with zipfile.ZipFile(archive) as zf:
            zf.extractall(RAW_DIR)
        archive.unlink()  # распаковали — архив больше не нужен
        print("Архив распакован и удалён.")

    # 5. Финальная проверка: все ли ключевые файлы на месте.
    still_missing = [f for f in KEY_FILES if not (RAW_DIR / f).exists()]
    if still_missing:
        sys.exit(f"После скачивания отсутствуют файлы: {', '.join(still_missing)}")
    print("Готово. Файлы в data/raw/:")
    for f in sorted(RAW_DIR.iterdir()):
        print(f"  - {f.name} ({f.stat().st_size / 1e6:.1f} МБ)")


if __name__ == "__main__":
    main()
