# Python bazel + gRPC

This is a very failure trial. There are too few users for such workflow. It doesn't work. Stop using bazel for it.

But I solved it with the solution here! (doesn't work unfortunately)

[Solution](https://github.com/grpc/grpc/issues/25082#issuecomment-754718296)
```
mkdir grpctest
cd grpctest
/usr/bin/python3 -m pip install virtualenv
/usr/bin/python3 -m virtualenv venv
source venv/bin/activate __
arch -x86_64 pip install --upgrade pip setuptools
arch -x86_64 pip install grpcio
arch -x86_64 pip install grpcio-tools
touch test.proto
...
arch -x86_64 python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. test.proto
touch main.py
arch -x86_64 python main.py
```

Some other discussion here: https://github.com/grpc/grpc/issues/24677

I tried 