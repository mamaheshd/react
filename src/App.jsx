// this is jsx code 
import './App.css';
// import {  legacy_createStore } from 'redux';
import { Provider } from 'react-redux'; // to pass data from 
// import testReducer from './reducers/testReducer';
import Test from './Test';
import Student from './Student';
import store from './store';
import Products from './Products';
import SingleProduct from './SingleProduct';
import Photos from './Photos';

function App() {
  // const store=legacy_createStore(testReducer)
  return (
    <Provider store={store}>
      <Test/>
      <Photos/>
      <Student/>
      <Products/>
      <SingleProduct/>
    </Provider>
  );
}

export default App;
