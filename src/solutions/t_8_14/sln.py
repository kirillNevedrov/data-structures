from typing import List


class Node:
    def get_value(self) -> int:
        pass

    def to_str(self) -> str:
        pass


class ConstantNode(Node):
    def __init__(self, value: str) -> None:
        self.value = int(value)

    def get_value(self) -> int:
        return self.value

    def to_str(self) -> str:
        return str(self.value)


class Operator:
    def __init__(self, value: str) -> None:
        self.value = value


class ExpressionNode(Node):
    def __init__(self, left_node: Node, right_node: Node, operator: Operator) -> None:
        if (
            not isinstance(left_node, Node)
            or not isinstance(right_node, Node)
            or not isinstance(operator, Operator)
        ):
            raise Exception(
                f"Unexpected node types: {type(left_node), type(right_node), type(operator)}"
            )

        self.left_node = left_node
        self.right_node = right_node
        self.operator = operator

    def get_value(self) -> int:
        left_value = self.left_node.get_value()
        right_value = self.right_node.get_value()

        if self.operator.value == "|":
            return left_value | right_value

        if self.operator.value == "&":
            return left_value & right_value

        if self.operator.value == "^":
            return left_value ^ right_value

        raise Exception(f"Operator {self.operator.value} is not supported")

    def to_str(self) -> str:
        return f"({self.left_node.to_str()} {self.operator.value} {self.right_node.to_str()})"


def count_eval(exp: str, res: bool) -> int:
    constants = ["0", "1"]
    operators = ["|", "&", "^"]

    nodes = []
    for c in exp:
        if c in constants:
            nodes.append(ConstantNode(c))
        elif c in operators:
            nodes.append(Operator(c))

    expressions = generate_expressions([nodes])
    expressions = [e for e in expressions if e.get_value() == res]

    return len(expressions)


def generate_expressions(expressions: List[List[Node]]) -> List[ExpressionNode]:
    if all(len(e) == 1 for e in expressions):
        return list({e[0].to_str(): e[0] for e in expressions}.values())

    new_expressions = []
    for e in expressions:
        for i in range(0, len(e) - 1, 2):
            new_expression = (
                e[:i]
                + [
                    ExpressionNode(
                        left_node=e[i], right_node=e[i + 2], operator=e[i + 1]
                    )
                ]
                + e[i + 3 :]
            )
            new_expressions.append(new_expression)

    return generate_expressions(new_expressions)
