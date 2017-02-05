# wlcd
wc -l clone in Python, plus support directory as argument

# install

```
pip install wcld
```

# Usage

Show total lines count of all files in current directory (``.``):

```
$ wcld .
212: .
```

Show only total lines count of python files (.py):

```
$ wcld -t py  # chose filetype .py
82: .
```

Show lines count of each file:

```
$ wcld -t py --debug
16: ./setup.py
66: ./wcld.py
82: .
```

Show lines count of all sub-directories under a path, do not count protobuf
generated files (``*.pb.go``) and test codes ``*_test.go``:

```
$ wcld github.com/influxdata/* -t go --exclude '*.pb.go, *_test.go'
    201: github.com/influxdata/config
  71695: github.com/influxdata/influxdb
 232527: github.com/influxdata/kapacitor
  43749: github.com/influxdata/telegraf
   4448: github.com/influxdata/toml
    166: github.com/influxdata/wlog
```

Why kapacitor is that big? Find out the reason:

```
$ wcld github.com/influxdata/kapacitor -t go --exclude '*.pb.go, *_test.go' -d | sort -nr | head
 232527: github.com/influxdata/kapacitor
   9664: github.com/influxdata/kapacitor/vendor/github.com/influxdata/influxdb/influxql/iterator.gen.go
   4795: github.com/influxdata/kapacitor/vendor/github.com/influxdata/influxdb/influxql/ast.go
   3154: github.com/influxdata/kapacitor/vendor/github.com/gogo/protobuf/protoc-gen-gogo/generator/generator.go
   2931: github.com/influxdata/kapacitor/vendor/github.com/influxdata/influxdb/influxql/parser.go
```

Oh because they commit ``vendor`` directory. Exclude that out:

```
$ wcld github.com/influxdata/kapacitor -t go --exclude '*.pb.go, *_test.go, */vendor/*'
  46407: github.com/influxdata/kapacitor
```

# Author

hvn@familug.org
