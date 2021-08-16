import React from "react";
import "./App.css";
import Axios from "axios";
import ChoiceForm from "./components/ChoiceForm";
function App() {
  const [questions, setQuestions] = React.useState<any[]>();

  React.useEffect(() => {
    Axios.get("http://localhost:8000/polls/questions/")
      .then((res) => {
        console.log(res.data);
        setQuestions(res.data);
      })
      .catch((err) => {
        console.log(err);
      });

  }, []);

  return (
    <div className="App">
      {questions?.map((question, index) => (
        <div key={question.id}>
          <h1>
            {index + 1}. {question.question_text}
          </h1>
          <ChoiceForm choices={question.choices} />
        </div>
      ))}
    </div>
  );
}

export default App;
