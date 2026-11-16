# Changelog

Все заметные изменения проекта документируются в этом файле.
Формат основан на [Keep a Changelog](https://keepachangelog.com/ru/1.1.0/),
версии — по [Semantic Versioning](https://semver.org/lang/ru/).

## [0.2.0] — 2026-11-16
### Added
- Ноутбук 01_data_overview.ipynb: первичный обзор M5 — размерности, wide→long, границы периода, топ-5 магазинов, доля топ-5 магазинов от общих продаж

## [0.1.0] — 2026-11-15
### Added
- Структура репозитория: data/, notebooks/, src/, tests/, reports/
- `download_data.py` — скачивание датасета M5 Forecasting с Kaggle
- README: постановка задачи, инструкция воспроизведения, роадмап, таблица результатов
- CI (GitHub Actions): установка зависимостей + smoke-тест импортов
