import { combineReducers } from "redux";
import testReducer from "./reducers/testReducer";
import stusentReducer from "./reducers/studentReducer";
import { legacy_createStore } from "redux";

const reducer=combineReducers({
    test:testReducer,
    student:stusentReducer
})

const store=legacy_createStore(reducer)

export default store
