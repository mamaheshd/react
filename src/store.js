import { combineReducers } from "redux";
import testReducer from "./reducers/testReducer";
import studentReducer from "./reducers/studentReducer";
import { legacy_createStore,applyMiddleware } from "redux";
import { thunk } from "redux-thunk";
import productReducer, { singleProductReducer } from "./reducers/productReducer";
import photoReducer from "./reducers/photoReducer";
import { cartReducer } from "./reducers/cartReducer";

const reducer=combineReducers({
    test:testReducer,
    student:studentReducer,
    productsData:productReducer,
    product:singleProductReducer,
    photosData:photoReducer,
    cart:cartReducer
})

const store=legacy_createStore(reducer,applyMiddleware(thunk)) //middlewere checks whether it is secure or not it allow or deallow to go forward

export default store
