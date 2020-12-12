default:
  cargo build --release

distclean:
  cargo clean

install:
	mkdir -p $(DESTDIR)/usr/bin
	cp target/release/package-test $(DESTDIR)/usr/bin
