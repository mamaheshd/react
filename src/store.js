import { combineReducers } from "redux";
import testReducer from "./reducers/testReducer";
import studentReducer from "./reducers/studentReducer";
import { legacy_createStore } from "redux";

const reducer=combineReducers({
    test:testReducer,
    student:studentReducer
})

const store=legacy_createStore(reducer)

export default store
