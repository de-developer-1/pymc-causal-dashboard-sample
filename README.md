# ベイズ推定による施策効果の可視化ダッシュボード

## 概要
このプロジェクトは、PyMC + ArviZ を使って施策の効果（uplift）をベイズ統計で推定し、Streamlit で可視化するダッシュボードテンプレート

## セットアップ手順

```bash
git clone git@github.com:de-developer-1/pymc-causal-dashboard-sample.git
cd pymc-causal-dashboard-sample
python data/generate_data.py  # サンプルデータ生成
docker compose up --build
```

## 構成
- `data/`: サンプルCSVと生成スクリプト
- `notebooks/`: PyMC + ArviZ による分析ノートブック
- `app/`: Streamlit アプリ
- `Dockerfile` + `docker-compose.yml`: Docker 実行環境
- `requirements.txt`: Python依存パッケージ