# LangChain Streamlit App

## 概要

このリポジトリは、LangChain を利用した Streamlit アプリケーションのサンプルです。LangChain は自然言語理解と生成に特化したライブラリで、このアプリケーションでは LangChain の機能を Streamlit インターフェースで簡単に試すことができます。

## 機能

- ユーザー入力に基づいて LangChain がテキスト生成
- 複数の生成モデルを選択可能
- インタラクティブな UI で直感的な操作

## 必要条件

- Python 3.7 以上
- Streamlit
- LangChain

## インストール方法

1. このリポジトリをクローンする
   ```
   git clone https://github.com/s-hiraoku/langchain-streamlit-app.git
   ```
2. 必要なライブラリをインストールする
   ```
   pip install -r requirements.txt
   ```

## 使用方法

1. Streamlit アプリを起動する
   ```
   streamlit run app.py
   ```
2. ブラウザで開くと、アプリのインターフェースが表示される
3. モデルとテキストを選択し、生成を行う

## ライセンス

このプロジェクトは[MIT ライセンス](LICENSE)の下で公開されています。
