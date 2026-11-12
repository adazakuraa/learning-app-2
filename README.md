# learning-app-2

学習アプリ（[learning-app](https://github.com/adazakuraa/learning-app)）の動画置き場です。
GitHub Pages は 1 サイト 1GB までなので、動画を 2 つのサイトに分けています。

- どの科目をここに置くかは learning-app の `content/video-hosts.yaml` で決めます。
- このリポジトリには動画ファイルを保存しません。`Publish videos` ワークフローが
  learning-app の main ブランチから該当科目の `video.mp4` を集めて
  `https://adazakuraa.github.io/learning-app-2/videos/<単元ID>.mp4` として公開します。
- 毎時、learning-app の main に変更があれば自動で公開し直します。
  learning-app にマージした直後にすぐ反映したいときは Actions から手動実行してください。
