import { combineReducers } from "redux";
import testReducer from "./reducers/testReducer";
import studentReducer from "./reducers/studentReducer";
import { legacy_createStore,applyMiddleware } from "redux";
import { thunk } from "redux-thunk";

const reducer=combineReducers({
    test:testReducer,
    student:studentReducer
})

const store=legacy_createStore(reducer,applyMiddleware(thunk)) //middlewere checks whether it is secure or not it allow or deallow to go forward

export default store
