# State Management Comparison — React + Redux, Angular + NgRx, Vue + Pinia

## React + Redux Toolkit

- **Boilerplate**: Minimal with RTK. `createSlice` generates action creators and reducers together. `createAsyncThunk` removes manual loading/error state handling.
- **Learning curve**: Medium. Core concepts (actions, reducers, selectors, thunks) take time to internalise but pay off in large apps.
- **Tooling**: Redux DevTools gives a full action log and state diff — excellent for debugging time-travel.
- **Pattern**: Centralised single store. Components connect via `useSelector` (read) and `useDispatch` (write). Selectors decouple components from state shape.

## Angular + NgRx

- **Boilerplate**: High. Requires separate files for Actions, Reducers, Effects, and Selectors. The pattern is strict by design — every async operation goes through an Effect, keeping reducers pure.
- **Learning curve**: Steep. RxJS knowledge is a prerequisite for Effects.
- **Tooling**: Redux DevTools compatible. Angular CLI generates NgRx scaffolding.
- **Pattern**: Same Redux unidirectional data flow, but enforced more rigidly. Effects are the key differentiator — they handle all side effects (API calls, routing) outside of components and reducers entirely.

## Vue + Pinia

- **Boilerplate**: Minimal. `defineStore` with the Composition API style needs only `ref`, `computed`, and plain functions — no action type constants, no separate reducer files.
- **Learning curve**: Low. Feels like writing a composable. Familiar to anyone who knows Vue's Composition API.
- **Tooling**: Vue DevTools Pinia tab shows state, actions, and timeline. `storeToRefs` is the one gotcha — forgetting it breaks reactivity on destructure.
- **Pattern**: Multiple focused stores (one per domain) rather than one root store. Stores can call each other directly, which is simpler but requires discipline to avoid circular dependencies.

## Key Differences Summary

| Concern            | Redux Toolkit     | NgRx                  | Pinia               |
|--------------------|-------------------|-----------------------|---------------------|
| Async handling     | createAsyncThunk  | Effects (RxJS)        | async actions       |
| Boilerplate        | Low               | High                  | Very low            |
| DevTools           | Redux DevTools    | Redux DevTools        | Vue DevTools        |
| Store structure    | Single root store | Single root store     | Multiple stores     |
| RxJS required      | No                | Yes                   | No                  |
| Learning curve     | Medium            | Steep                 | Low                 |
