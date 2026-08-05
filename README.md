# Cobalt Development Repository

> 🚧 **Development Branch** - main development repository for Cobalt

## About Cobalt

Cobalt is an async-first web framework with typed route handlers.

## 🔧 Development Status

This repository is under active development. Many features are TODO.

### 🔴 High Priority TODOs

- Core functionality is still being implemented across modules.

### 📝 Complete TODO List

- [ ] **cobalt/middleware/auth.py:3** - validate JWT signature and expiry
- [ ] **cobalt/routing/router.py:3** - support path parameter type converters
- [ ] **cobalt/routing/router.py:4** - cache compiled route patterns
- [ ] **cobalt/routing/router.py:8** - return 405 for method mismatch vs 404
- [ ] **cobalt/serialize/json.py:2** - handle dataclasses and enums
- [ ] **cobalt/serialize/json.py:10** - add msgpack serialization backend

## 🤝 Contributing

1. Pick a TODO item from the list above
2. Implement the functionality
3. Update this README when TODOs are completed
