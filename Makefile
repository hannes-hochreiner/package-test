default:
	curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
  cargo build --release

distclean:
  cargo clean

install:
	mkdir -p $(DESTDIR)/usr/bin
	cp target/release/package-test $(DESTDIR)/usr/bin
