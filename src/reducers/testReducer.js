const initialValue={
    count:0
}

const testReducer=(state=initialValue,action)=>{ //action and state are parameters 
    switch(action.type){
        case 'ADD_ITEM':
            return{
                count:++state.count //added from current state
            }
        default:
            return state
    }
}

export default testReducer