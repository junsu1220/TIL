import styled from "styled-components";
import { Line } from "react-chartjs-2";
import { Chart as ChartJS } from "chart.js/auto"; //미사용하지만 안적어주면 오류남
const Chart001 = ({ customerGraph }) => {

	const chartData001 = {
    labels: customerGraph.labels,
    datasets: [
      {
        type: "line",
        label: "Dataset 1",
        borderColor: "#1b1111",
        borderWidth: 2,
        data: customerGraph.data,
      },
    ],
  };

	const chartOptions001 = {
		
	}

	return (
	    <Container>
	      <Line
	        type="line"
	        data={chartData001}
	        options={chartOptions001}
	        width="450px"
	      />
	    </Container>
	  );
	};

export default Chart001;

const Container = styled.div`
  height: 200px;
  width: 100%;
  display: flex;
  justify-content: center;
`;
