# dwc
[![CircleCI](https://circleci.com/gh/hvnsweeting/dwc.svg?style=svg)](https://circleci.com/gh/hvnsweeting/dwc)

wc -l clone in Python, plus support directory as argument

# install

```
pip install dwc
```

# Usage

Show total lines count of all files in current directory (``.``):

```
$ dwc .
212: .
```

Show only total lines count of python files (.py):

```
$ dwc -t py  # chose filetype .py
82: .
```

Show lines count of each file:

```
$ dwc -t py --debug
16: ./setup.py
66: ./dwc.py
82: .
```

Show lines count of all sub-directories under a path, do not count protobuf
generated files (``*.pb.go``) and test codes ``*_test.go``:

```
$ dwc github.com/influxdata/* -t go --exclude '*.pb.go, *_test.go'
    201: github.com/influxdata/config
  71695: github.com/influxdata/influxdb
 232527: github.com/influxdata/kapacitor
  43749: github.com/influxdata/telegraf
   4448: github.com/influxdata/toml
    166: github.com/influxdata/wlog
```

Why kapacitor is that big? Find out the reason:

```
$ dwc github.com/influxdata/kapacitor -t go --exclude '*.pb.go, *_test.go' -d | sort -nr | head
 232527: github.com/influxdata/kapacitor
   9664: github.com/influxdata/kapacitor/vendor/github.com/influxdata/influxdb/influxql/iterator.gen.go
   4795: github.com/influxdata/kapacitor/vendor/github.com/influxdata/influxdb/influxql/ast.go
   3154: github.com/influxdata/kapacitor/vendor/github.com/gogo/protobuf/protoc-gen-gogo/generator/generator.go
   2931: github.com/influxdata/kapacitor/vendor/github.com/influxdata/influxdb/influxql/parser.go
```

Oh because they commit ``vendor`` directory. Exclude that out:

```
$ dwc github.com/influxdata/kapacitor -t go --exclude '*.pb.go, *_test.go, */vendor/*'
  46407: github.com/influxdata/kapacitor
```

Find out shortest implementations of [Make a LISP](https://github.com/kanaka/mal)

```
$ dwc mal/*/ | sort -n | head
    494: mal/examples/
    846: mal/docs/
   1268: mal/mal/
   1464: mal/perl6/
   1483: mal/coffee/
   1509: mal/io/
   1534: mal/racket/
   1571: mal/ocaml/
   1579: mal/es6/
   1621: mal/factor/
```

So `mal` is the best, then `perl6` and `coffee` in term of shortest
implementations.

# Use case
Are you writing micro services?  If each service implementation contains more
than 3000 lines of code, is that still micro service anyway?

# Author

hvn@familug.org
