.PHONY: default

INSTALL = install
INSTALL_PROGRAM = $(INSTALL)

prefix = /usr
exec_prefix = $(prefix)
bindir = $(exec_prefix)/bin

default:
	cargo build --release

	$(INSTALL_PROGRAM) -D target/release/foo $(DESTDIR)$(bindir)/foo
