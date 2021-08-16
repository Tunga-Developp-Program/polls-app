import React from "react";
import Axios from "axios";

const ChoiceForm = ({ choices }: any) => {
  const [selected, setSelected] = React.useState("");

  const formSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    console.log(selected);
    const choice = await Axios.get(
      `http://localhost:8000/polls/choices/${selected}/`
    );
    console.log({ choice: choice.data });

    const votes = await Axios.patch(
      `http://localhost:8000/polls/choices/${choice.data.id}/`,
      { votes: choice.data.votes + 1 }
    );
    console.log(votes.data);
  };
  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    console.log(e.target.value);
    setSelected(e.target.value);
  };
  return (
    <form onSubmit={formSubmit}>
      {choices?.map((choice: any) => (
        <p key={choice.id}>
          <label htmlFor="choices">
            <input
              type="radio"
              name="choices"
              id=""
              value={choice.id}
              onChange={handleChange}
            />
            {choice.choice_text}
          </label>
        </p>
      ))}
      <input type="submit" value="Save" />
    </form>
  );
};
export default ChoiceForm;
