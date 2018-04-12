# Gitのテスト用レポジトリ

## checkout
```
git checkout -b [ローカルブランチ名] origin/[リモートブランチ名]：リモートブランチ
```

## push
```
git push {ローカルのhoge}:{リモートのhoge}
```

## rebase
```
git rebase -i {修正したいcommitの1つ前のcommit ID}
修正したいcommitのpick を editに変更、保存
完了したら以下のコマンド修正をcommit
git commit --amend
修正が完了したら以下のコマンドで修正する
git rebase --continue
```

## fetch
```
git fetch origin {リモート}:{ローカル}
```

## stash

```
git stash save
```
で退避


```
git status
```

でステージングされているファイルを見ると、変更状態のファイルがなくなっているのが確認できる。

stashしているファイルの確認
```
git stash list
```

変更内容の確認

```
git stash list -p
```

stashしているファイルの復活
```
git stash apply stash@{0}
```

stashの削除
```
git stash drop <消したいstash名>
```

変更の復活と、削除を同時に行う。
```
git stash pop stash@{0}
```
