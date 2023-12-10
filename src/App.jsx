// this is jsx code 
import logo from './logo.svg';  
import './App.css';
import {  legacy_createStore } from 'redux';
import { Provider } from 'react-redux'; // to pass data from 
import testReducer from './reducers/testReducer';
import Test from './Test';

function App() {
  const store=legacy_createStore(testReducer)
  return (
    <Provider store={store}>
      <Test/>

    </Provider>
  );
}

export default App;
