'''
Created on Dec 3, 2020

@author: areid
'''
def writeSolutions(outputFolder, teamName="Epsilon", problem, solutions):
    
    
    
# public static void writeSolutions(String outputFolder, String teamName, TravelingThiefProblem problem, List<Solution> solutions) throws IOException {
# 
#         int numberOfSolutions = Competition.numberOfSolutions(problem);
#         if (solutions.size() > numberOfSolutions) {
#             System.out.println(String.format("WARNING: Finally the competition allows only %s solutions to be submitted. " +
#                     "Your algorithm found %s solutions.", numberOfSolutions, solutions.size()));
#         }
# 
#         BufferedWriter varBw = Files.newBufferedWriter(Paths.get(outputFolder,
#                 String.format("%s_%s.x", teamName, problem.name)));
# 
#         BufferedWriter objBw = Files.newBufferedWriter(Paths.get(outputFolder,
#                 String.format("%s_%s.f", teamName, problem.name)));
# 
# 
#         for (Solution solution : solutions) {
# 
#             // add one to the index of each city to match the index of the input format
#             List<Integer> modTour = new ArrayList<>(solution.pi);
#             for (int i = 0; i < modTour.size(); i++) {
#                 modTour.set(i, modTour.get(i) + 1);
#             }
# 
#             // write the variables
#             varBw.write(String.join(" ",
#                     modTour.stream().map(Object::toString).collect(Collectors.toList())) + "\n");
#             varBw.write(String.join(" ",
#                     solution.z.stream().map(b -> b ? "1" : "0").collect(Collectors.toList())) + "\n");
#             varBw.write("\n");
# 
#             // write into the objective file
#             objBw.write(String.format("%.16f %.16f", solution.time, solution.profit) + "\n");
# 
#         }
# 
#         varBw.close();
#         objBw.close();
# 
# 
# 
#     }