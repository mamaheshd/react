const initialValue={
    count:0
}

const testReducer=(state=initialValue,action)=>{ //action and state are parameters 
    switch(action.type){
        case 'ADD_ITEMS':
            return{
                count:++state.count //added from current state
            }
        case 'DEC_ITEMS':
            return{
                count:--state.count
            }
        default:
            return state
    }
}

export default testReducer