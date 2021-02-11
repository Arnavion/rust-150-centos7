Repro for Rust 1.50.0 failure on CentOS 7

```sh
git clone github.com:Arnavion/rust-150-centos7
cd rust-150-centos7
docker run -it --rm -v "$PWD:/foo-1.0.0" centos:7
```

Inside the Docker shell:

```sh
yum install -y curl gcc make rpm-build

mkdir -p ~/.cargo/bin
export PATH="$PATH:$(realpath ~/.cargo/bin)"

curl -Lo ~/.cargo/bin/rustup 'https://static.rust-lang.org/rustup/dist/x86_64-unknown-linux-gnu/rustup-init'
chmod +x ~/.cargo/bin/rustup
hash -r

rustup set profile minimal
rustup install 1.49.0

RPMBUILDDIR="$HOME/rpmbuild"
mkdir -p "$RPMBUILDDIR/SOURCES"

tar -cvzf "$RPMBUILDDIR/SOURCES/foo-1.0.0-1.tar.gz" /foo-1.0.0


mkdir -p "$RPMBUILDDIR/SPECS"
cp /foo-1.0.0/foo.spec "$RPMBUILDDIR/SPECS/foo.spec"

rpmbuild -ba "$RPMBUILDDIR/SPECS/foo.spec"
```

The `rpmbuild` command fails with:

```
...

cargo build --release
   Compiling foo v0.1.0 (/root/rpmbuild/BUILD/foo-1.0.0)
    Finished release [optimized] target(s) in 0.42s
install -D target/release/foo /root/rpmbuild/BUILDROOT/foo-1.0.0-1.x86_64/usr/bin/foo
+ /usr/lib/rpm/find-debuginfo.sh --strict-build-id -m --run-dwz --dwz-low-mem-die-limit 10000000 --dwz-max-die-limit 110000000 /root/rpmbuild/BUILD/foo-1.0.0
extracting debug info from /root/rpmbuild/BUILDROOT/foo-1.0.0-1.x86_64/usr/bin/foo
/usr/lib/rpm/debugedit: canonicalization unexpectedly shrank by one character
error: Bad exit status from /var/tmp/rpm-tmp.y1gaix (%install)


RPM build errors:
    Bad exit status from /var/tmp/rpm-tmp.y1gaix (%install)
```
